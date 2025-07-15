import { useState, useEffect } from "react"
import { setUser } from '../utils/auth'

function MainWrapper({ children }) {
    const [loading, setLoading] = useState(true)
    
    useEffect( async () => {
        const handler = async () => {
            setLoading(true)
             
            // get token if not get new access token ans set user info in {}
            await setUser()
            setLoading(false)
        }
        handler()
    }, [])

  return (
    <div>
        {loading ? null : children}
    </div>
  )
}

export default MainWrapper
