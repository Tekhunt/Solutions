import React from "react";
import './style.css'


function SignUpButton({action, type}){
    return (
        <button className="signUpButton" id="sup-btn" type={type}>{action}</button>
    )
}

export default SignUpButton