import React, {useState} from "react";
import './style.css'
import Toggle from './Toggle'


function PasswordField({label, type, password, change}){
    const [toggle, setToggle] = useState(true)
    return (
        <form className="form-field">
        <div className="labels">
            <p className="name">{label}:</p>
            <Toggle toggle={toggle} updateToggle={() => setToggle(!toggle)} />
        </div>
       
        <input type={toggle ? "text" : type} value={password} onChange={change}></input>
        </form>
    )
}

export default PasswordField;