import React, { useState, useEffect } from "react";
import Image from "../../Assests/image1.svg";
import { Wrapper, Input } from "./registerStyle";
import axios from "axios";
import { useHistory } from "react-router";
import { toast } from "react-toastify";
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";

const eye = <FontAwesomeIcon icon={faEye} />;
const eyeslash = <FontAwesomeIcon icon={faEyeSlash} />;
const url = "https://bouncerb.herokuapp.com/api/v1/register/";

function Register() {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState(null);
  const history = useHistory();
  const [passwordShown, setPasswordShown] = useState(false);
  const [redirect, setRedirect] = useState(false);

  useEffect(() => {
    if (redirect) {
      history.push("/login");
    }
  }, [redirect, history]);

  const togglePasswordVisiblity = () => {
    setPasswordShown(passwordShown ? false : true);
  };

  const handleSubmit = (e) => {
    const datas = { first_name, last_name, email, password };
    e.preventDefault();

    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    axios
      .post(url, datas, config)
      .then(
        (response) => {
          toast(
            "Registration Successful. Check your Email to confirm your account",
            { type: "success" }
          );
          setRedirect(true);
        },
        (err) => {
          if (err.response.status === 400) {
            toast("Registration Failed. Use a valid Email ", { type: "error" });
          }
        }
      )
      .catch((err) => {
        console.log("Axios Error:", err);
        setError(error);
        toast("Bad request", { type: "error" });
      });
  };
  return (
    <Wrapper>
      <div className="header">
        <Link to="/"><h1 className="logo">BOUNCER</h1></Link>
      </div>

      <div className="container">
        <div className="image">
          <img className="img" src={Image} alt="bouncer" />
        </div>
        <div className="register">
          <form className="" onSubmit={handleSubmit}>
            <div className="reg-header">
             <Link to='/login'> <button className="sign">Sign In</button></Link>
              <button className="reg">Register </button>
            </div>
            <label>
              First name:
              <Input
                className="dinput"
                type="text"
                value={first_name}
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
            </label>
            <label>
              Last name:
              <Input
                className="dinput"
                type="text"
                value={last_name}
                onChange={(e) => setLastName(e.target.value)}
                required
              />
            </label>
            <label>
              Username:
              <Input
                className="dinput"
                type="text"
                value={username}
                onChange={(e) => setUserName(e.target.value)}
                required
              />
            </label>
            <label>
              Email:
              <Input
                className="dinput"
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </label>
            <label>
              <div className="passEye">
                Password:
                <i className="eye" onClick={togglePasswordVisiblity}>
                  {passwordShown ? eye : eyeslash}
                </i>
              </div>
              <Input
                className="dinput"
                type={passwordShown ? "text" : "password"}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </label>
            <label>
              <div className="passEye">
                confirm password:
                <i className="eye" onClick={togglePasswordVisiblity}>
                  {passwordShown ? eye : eyeslash}
                </i>
              </div>
              <Input
                className="dinput"
                type={passwordShown ? "text" : "password"}
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
            </label>

            <label>
              <Input className="button" type="submit" value="Sign Up" />
            </label>
          </form>{" "}
          <br />
          <div className="footer">
            <button className="sign">Become a vendor</button>
            <button className="pass">Forgot password</button>
          </div>
        </div>
      </div>
    </Wrapper>
  );
}

export default Register;
