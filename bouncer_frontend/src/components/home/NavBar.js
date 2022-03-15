import React from 'react'
import { Link } from 'react-router-dom';
import { NavBarWrapper  } from './NavBarStyled';

function NavBarPage() {
    return (
        <NavBarWrapper>
            <nav>
                <div>
                    <Link href="/">HOME</Link>
                    <div className="right-menu">
                        <Link href="/">STORE</Link>
                        <div className="dropdown-menu">
                            <div>
                                <div class="stage-one">
                                    <h4>Category</h4>
                                    <Link href="/">AirPort & Wireless</Link> <br />
                                    <Link href="/">AppleCare</Link> <br />
                                    <Link href="/">Bags, Shells & Sleeves</Link> <br />
                                    <Link href="/">Business & Security</Link> <br />
                                    <Link href="/">Cables & Docks</Link>
                                </div>
                                <div class="stage-two">
                                    <h4>Category</h4>
                                    <Link href="/">Camera & Video</Link><br />
                                    <Link href="/">Car & Travel</Link> <br />
                                    <Link href="/">Cases & Films</Link>
                                </div>
                                <div class="stage-three">
                                    <h4>Category</h4>
                                    <Link href="/">Charging Devices</Link> <br />
                                    <Link href="/">Connected Home</Link> <br />
                                    <Link href="/">Device Care</Link> <br />
                                    <Link href="/">Display & Graphic</Link> <br />
                                    <Link href="/">Fitness & Sport</Link>
                                </div>
                                <div class="stage-four"><h4>Category</h4>
                                    <Link href="/">Headphones</Link> <br />
                                    <Link href="/">HealhKit</Link></div>
                                <div class="stage-five">
                                    <h4>Category</h4>
                                    <Link href="/">Mics & Keyboards</Link> <br />
                                    <Link href="/">Music Creation</Link> <br />
                                    <Link href="/">Networking & Server</Link>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <Link href="/">IPHONE</Link>
                    <Link href="/">IPAD</Link>
                    <Link href="/">MACBOOK</Link>
                    <Link href="/">ACCESSORIES</Link>
                
                </div>
            </nav> 
        </NavBarWrapper>
    )
}

export default NavBarPage;