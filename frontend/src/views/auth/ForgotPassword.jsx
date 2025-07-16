import { useState } from "react"
import apiInstance from "../../utils/axios";
import { useNavigate } from "react-router-dom";


function ForgotPassword() {
    const [email, setEmail] = useState("")
    const navigate = useNavigate()
    const handleSubmit = async () => {
        try {
            await apiInstance.get(`user/password-reset/${email}/`).then((res) => {
                navigate("/create-new-password")

            })
        } catch (error) {
            alert("Email not exist")
        }
    }

    return (
    <div>
        <h1>Forgot Password</h1>
        <input type='email' placeholder='Enter Email'
            onChange={(e) => setEmail(e.target.value)} />
        <br />
        <button onClick={handleSubmit} type='submit'>Reset Password</button>
    </div>
  )
}

export default ForgotPassword
