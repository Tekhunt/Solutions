import React from "react";
import { Link } from 'react-router-dom';
import './style.css'

function Header(){
    return (
        <Link to='/'><h1 class="bouncer-header">BOUNCER</h1></Link>
    )
}

export default Header;