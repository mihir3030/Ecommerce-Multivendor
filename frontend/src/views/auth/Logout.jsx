import { useEffect } from "react"
import { logout } from "../../utils/auth"
import { Link } from "react-router-dom"


function Logout() {
    useEffect(() => {
        logout()
    }, [])
  return (
   <section>
    <main className="" style={{ marginBottom: 100, marginTop: 50 }}>
        <div className="container">
            {/* Section: Login form */}
            <section className="">
                <div className="row d-flex justify-content-center">
                    <div className="col-xl-5 col-md-8">
                        <div className="card rounded-5">
                            <div className="card-body p-4 text-center">
                                <h3> You Have Benn Logged Out</h3>
                                  <Link to={"/register"} className="btn btn-primary">Register
                                    <i className="fas fa-user-plus"></i>
                                  </Link>
                                  <Link to={"/login"} className="btn btn-primary">Sign In
                                    <i className="fas fa-sign-in"></i>
                                  </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </main>
</section>
  )
}

export default Logout
