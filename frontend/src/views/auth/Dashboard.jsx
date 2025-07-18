import { useAuthStore } from "../../store/auth";
import { Link } from "react-router-dom";

function Dashboard() {
  const [isLoggedIn, setIsLoaggedIn] = useAuthStore((state) => [
    state.isLoggedIn,
    state.user,
  ]);
  return (
    <>
      {isLoggedIn() ? (
        <div>
          <h2>Dashboard</h2>
          {/* Link is like <a> tage  */}
          <Link  to={"/logout"}>Logout</Link>
        </div>
      ) : (
        <div>
          <Link className="btn btn-primary" to={"/login"}>Login</Link>
          <Link className="btn btn-primary" to={"/register"}>Register</Link>
        </div>
      )}
    </>
  );
}

export default Dashboard;
