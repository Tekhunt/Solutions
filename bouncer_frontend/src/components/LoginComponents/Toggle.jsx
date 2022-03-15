import React from "react";
import './style.css'


function Toggle({toggle, updateToggle}){
    return (
        <p className="favicon"> <i class={toggle? "fa fa-eye": "fa fa-eye-slash"} aria-hidden="true" onClick={() => updateToggle()} ></i> </p>
       
    )
}

export default Toggle;