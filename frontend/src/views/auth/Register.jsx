import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import { useAuthStore } from "../../store/auth"
import { register } from "../../utils/auth"


function Register() {
    const [fullname, setFullname] = useState("")
    const [email, setEmail] = useState("")
    const [phone, setPhone] = useState("")
    const [password, setPassword] = useState("")
    const [password2, setPassword2] = useState("")
    const [isLoading, setIsLoading] = useState(false);

    const navigate = useNavigate()
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn) 

    useEffect(() => {
        if(isLoggedIn()){
            navigate("/")
        }
    }, [])  // whenever isLoading cvalue changes use effect runs

    const handleSubmit = async (e) => {
        e.preventDefault()
        setIsLoading(true)

        const {error} = await register(fullname, email, phone, password, password2)
        if(error) {
            alert(error)
        } else {
            navigate("/")
        }
    }

  return (
    <div>
      <h2> Register</h2>
      <form onSubmit={handleSubmit}>
        <input 
            type="text"
            placeholder="Full Name"
            name=""
            id="fullname"
            onChange={(e) => setFullname(e.target.value)}
            />
        <br /><br />
        <input 
            type="email"
            placeholder="email"
            name=""
            id="email"
            onChange={(e) => setEmail(e.target.value)}
            />

        <br /><br />
        <input 
            type="text"
            placeholder="Mobile Number"
            name=""
            id="mobile"
            onChange={(e) => setPhone(e.target.value)}
            />

        <br /><br />
        <input 
            type="password"
            placeholder="Password"
            name=""
            id="pasword"
            onChange={(e) => setPassword(e.target.value)}
            />

        <br /><br />
        <input 
            type="password"
            placeholder="Confirm Password"
            name=""
            id="password2"
            onChange={(e) => setPassword2(e.target.value)}
            />
        <br /><br />
        <button type="submit">Register</button>
      </form>
    </div>
  )
}

export default Register
