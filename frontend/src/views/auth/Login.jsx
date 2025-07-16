import { useState, useEffect } from "react";
import { login } from "../../utils/auth";
import { useNavigate, Link } from "react-router-dom";
import { useAuthStore } from "../../store/auth";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const isLoggedIn = useAuthStore((state) => state.isLoggedIn);

  const navigate = useNavigate();

  useEffect(() => {
    if (isLoggedIn()) {
      navigate("/dashboard");
    }
  }, []);

  // Reset Form reset valu of email and password
  const resetForm = () => {
    setEmail("");
    setPassword("");
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const { error } = await login(email, password);

    if (error) {
      alert(error);
    } else {
      navigate("/dashboard");
      resetForm();
    }
    setIsLoading(false);
  };

  return (
    <div>
      <h2>Welcome Back</h2>
      <p>Login To Continue</p>
      <form onSubmit={handleLogin}>
        <input 
            type="text" 
            name="email" 
            id="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value) } />
        <br />
        <input 
            type="password" 
            name="password" 
            id="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value) } />
        
        <br />

        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
