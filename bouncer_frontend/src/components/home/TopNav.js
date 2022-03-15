import React from 'react'
import { Link } from 'react-router-dom';
import { NavWrapper, SelectLang, SelectSpace, UserSection  } from "./TopStyled";


function TopNav() {
    return (  
        <NavWrapper className="top-header">
            <header className="container">
                <div className="top-nav">
                    <div className="lang-select">
                        <SelectLang name="Select" id="select">
                            <optgroup label="Select">
                                <option value="">EN</option>
                                <option value="">YR</option>
                                <option value="">FR</option>
                                <option value="">IG</option>
                            </optgroup>
                        </SelectLang>
                        <SelectSpace>
                            <SelectLang className="usd" name="" id="select">
                                <optgroup label="Select">
                                    <option value="">USD</option>
                                    <option value="">NGN</option>
                                    <option value="">YEN</option>
                                </optgroup>
                            </SelectLang>
                        </SelectSpace>
                    </div>
                    <UserSection className="profile-item">
                        <div className="profile-section">
                            <i className="fas fa-user-alt"></i>
                            <span><Link href="#" class="user-profile">My profile</Link></span>
                            <span className="basket-shopping"><i className="fas fa-shopping-basket"></i></span>0 items
                            <span className="amount-cart">$0.00</span>
                            <span className="search"><i class="fas fa-search"></i></span>
                        </div>
                    </UserSection>
                </div>
            </header>
        </NavWrapper>  
    )
};

export default TopNav;
