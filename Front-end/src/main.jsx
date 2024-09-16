import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "./index.css";
import Login from "./components/Login"
import MainLoader from "./components/MainLoader";
import RedirectComponent from "./components/RedirectComponent";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RedirectComponent/>,
  },
  {
    path:"login",
    element: <Login/>
  },
  {
    path:"dashboard",
    element: <MainLoader/>,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);