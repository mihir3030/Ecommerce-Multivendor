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
          <Link to={"/logout"}>Logout</Link>
        </div>
      ) : (
        <div>
          <Link to={"/login"}>Login</Link>
          <Link to={"/register"}>Register</Link>
        </div>
      )}
    </>
  );
}

export default Dashboard;
