import React from 'react'
import { Link } from 'react-router-dom';
import { ItemWrapper } from './NavItemStyled';

function NavItem() {
    return (
        <ItemWrapper>
            <div class="best-seller">
                <p>BEST SELLER</p>
            </div>
                <nav class="menu-bar">
                <ul>
                    <li><Link href="/">All</Link></li>
                    <li><Link href="/">Mac</Link></li>
                    <li><Link href="/">iPhone</Link></li>
                    <li><Link href="/">iPad</Link></li>
                    <li><Link href="/">Accessories</Link></li>
                </ul>
                </nav>
        </ItemWrapper>
    )
}

export default NavItem
