import { Navigate } from "react-router-dom";

function RedirectComponent() {
  // Use Navigate component for redirection
  return <Navigate to="/login" />;
}

export default RedirectComponent;
