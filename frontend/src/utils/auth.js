import { useAuthStore } from '../store/auth';
import axios from './axios';
import { jwtDecode } from 'jwt-decode';
import cookies from 'js-cookie';

// ✅ LOGIN
export const login = async (email, password) => {
  try {
    const { data, status } = await axios.post('/user/token/', { email, password });

    if (status === 200) {
      setAuthUser(data.access, data.refresh);
    }

    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error.response?.data?.detail || 'Something went wrong',
    };
  }
};

// ✅ REGISTER
export const register = async (full_name, email, phone, password, password2) => {
  try {
    const { data } = await axios.post('/user/register/', {
      full_name,
      email,
      phone,
      password,
      password2,
    });

    await login(email, password);
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error.response?.data?.detail || 'Something went wrong',
    };
  }
};

// ✅ LOGOUT
export const logout = () => {
  cookies.remove('access_token', { path: '/' });
  cookies.remove('refresh_token', { path: '/' });
  useAuthStore.getState().setUser(null);
};

// ✅ SET USER (on refresh)
export const setUser = async () => {
  const access_token = cookies.get('access_token');
  const refresh_token = cookies.get('refresh_token');

  if (!access_token || !refresh_token) return;

  const store = useAuthStore.getState();

  try {
    if (isAccessTokenExpired(access_token)) {
      const response = await getRefreshToken(refresh_token);
      setAuthUser(response.access, response.refresh);
    } else {
      setAuthUser(access_token, refresh_token);
    }
  } catch (error) {
    console.error('Failed to restore user session:', error);
    logout();
  } finally {
    store.setLoading(false);
  }
};

// ✅ SET AUTH USER (with cookies + Zustand)
export const setAuthUser = (access_token, refresh_token) => {
  cookies.set('access_token', access_token, { expires: 1, secure: true });
  cookies.set('refresh_token', refresh_token, { expires: 7, secure: true });

  try {
    const user = jwtDecode(access_token);
    if (user) {
      useAuthStore.getState().setUser(user);
    }
  } catch (err) {
    console.error('Failed to decode token', err);
  }
};

// ✅ REFRESH TOKEN
export const getRefreshToken = async (refresh_token) => {
  const response = await axios.post('/user/token/refresh/', {
    refresh: refresh_token,
  });

  return response.data;
};

// ✅ TOKEN EXPIRY CHECK (fixed math)
export const isAccessTokenExpired = (accessToken) => {
  try {
    const decoded = jwtDecode(accessToken);
    return decoded.exp < Date.now() / 1000;
  } catch (err) {
    console.error('Invalid access token', err);
    return true;
  }
};
