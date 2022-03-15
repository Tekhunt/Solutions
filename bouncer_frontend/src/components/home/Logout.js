import React from 'react'
import { Link } from 'react-router-dom';

function Logout() {
    
    const ClearLocalStorageItem = ()=> localStorage.clear();

    
    return (
        <div>
            <Link to ="/" onClick={ClearLocalStorageItem} >Logout</Link>
        </div>
    )
}
 export default Logout;