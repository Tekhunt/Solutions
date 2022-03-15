import React from "react";
import './style.css'
// import Toggle from './Toggle'

function InputField({label, type, username, change}){
    return (
        <form className="form-field">
        <div className="labels">
            <p className="name">{label}:</p>
        </div>
       
        <input type ={type} value={username} onChange={change}></input>
        </form>
    )
}

export default InputField;