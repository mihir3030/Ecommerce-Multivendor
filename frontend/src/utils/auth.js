import {useAuthStore} from '../store/auth'
import axios from './axios'
import jwt_decode from 'jwt-decode'
import cookies from 'js-cookie'
import Cookies from 'js-cookie'


// this is login function fetch data and print
export const login = async (email, password) => {
    try {
        // request to Djnago login
        const { data, status } = await axios.post("/user/token", {
            email,
            password
        })
        if (status === 200){
            // get access token and refresh token
            setAuthUser(data.access, data.refresh)   // set user info to Zustand Store.js
        }
        return {data, error: null}

    } catch (error) {
        return {
            data: null,
            error: error.response.data?.detail || "Somthing went wrong"
        }
    }
}


// this is for register user
export const register = async (full_name, email, phone, password, password2) => {
    try {
        const { data } = await axios.post("/user/register", {
            full_name, 
            email, 
            phone, 
            password, 
            password2
        })

        // after register automatically logged in
        await login(email, password)
        return {data, error: null}

    } catch (error) {
        return {
            data: null,
            error: error.response.data?.detail || "Somthing went wrong"
        }
    }
}


// user logout
export const logout = () => {
    cookies.remove("access_token")
    cookies.remove("refresh_token")

    // set user null in our store
    useAuthStore.getState().setUser(null)
}


export const setUser = async () => {
    const access_token = cookies.get("access_token")
    const refresh_token = cookies.get("refresh_token")

    // is not token return empty
    if (!access_token || !refresh_token) return;

    // is token expired get new one from refresh token and set user to Store.js
    if(isAccessTokenExpired(accessToken)){
        const response = await getRefreshToken(refreshToken)
        setAuthUser(response.access, response.refresh)
    }

    // if token not expired set user
    else {
        setAuthUser(accessToken, refreshToken)
    }
}



export const setAuthUser = (access_token, refresh_token) => {
    // set token in COOKIES
    cookies.set("access_token", access_token, {
        expires: 1,
        secure: true
    })
    cookies.set("refresh_token", refresh_token, {
        expires: 7,
        secure: true
    })

    // decode token - {id, name....} and assign in variable
    const user = jwt_decode(access_token) ?? null

    // if user not null setUser store.js
    if (user) {
        useAuthStore.getState().setUser(user)
    }
    useAuthStore.getState().setLoading(false)
}


export const getRefreshToken = async () => {
    //get refresh token
    const refresh_token = Cookies.get("refresh_token")

    // from current refresh token we get new access token from Django
    const response = await axios.post('user/token/refresh/', {
        refresh: refresh_token
    })

    return response.data
}


export const isAccessTokenExpired = (accessToken) => {
    try {
        const decodedToken = jwt_decode(accessToken)

        // check if access token expired and return True if expired so we get new accesToken
        return decodedToken.exp < Date.now() / 100
    } catch (error) {
        console.log(error);
        return true
    }
}