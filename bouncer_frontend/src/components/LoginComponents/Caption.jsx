import React from "react";
import {Link} from "react-router-dom";
import './style.css'
// import Register from "./Register";
// import $ from "jquery";
// import Login from "./Login";


function Caption({left, idleft, leftUrl, right, rightUrl}){

    return (
        <div >
            <div className="caption">
            <p className="cap1 cap" id={idleft}><Link to={`/${leftUrl}`}> {left} </Link></p>
            <p className="cap2 cap"> <Link to={`/${rightUrl}`}>{right}</Link></p>
            </div>
           
        </div>
    )
}

export default Caption;