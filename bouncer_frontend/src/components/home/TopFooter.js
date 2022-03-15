import React from 'react'
import { TopFooterWrapper } from './TopFooterStyled';
import { Link } from 'react-router-dom';

function TopFooter() {
    return (
        <TopFooterWrapper>
            <div className="container">
                <div className="footer-top">
                    <div>
                        <img src="img/logo.b701f098 (1).svg" alt="bouncer-logo" />
                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
                            standard dummy text ever.Since the 1500s, when an unknown printer.
                        </p>
                    </div>
                    <div>
                        <h4 className="footer-text">Follow Us</h4>
                        <p>Since the 1500s, when an unknown printer 
                            took a galley of type and scrambled.
                        </p>
                        <i className="fab fa-facebook-f"></i>
                    <span className="twitter-icon">
                        <i className="fab fa-twitter"></i>
                    </span>
                    </div>
                    <div>
                        <h4 className="footer-text">Contact Us</h4>
                        <p>
                            My Company , 4578 Marmora Road, <br/>
                            Glasgow D04 89GR <br />
                            Call us now: 0123-456-789 <br />
                            Email: support@whatever.com
                        </p>
                    </div>
                </div>
                <div className="footer-line">
                </div>
                <div className="footer-link">
                    <div>
                        <div>
                            <p>Information</p>
                            <Link href="/">About Us</Link> <br />
                            <Link href="/">Information</Link> <br />
                            <Link href="/">Privacy Policy</Link> <br />
                            <Link href="/">Terms & Conditions</Link>
                        </div>
                        <div>
                            <p>Services</p>
                            <Link href="/">About Us</Link> <br />
                            <Link href="/">Information</Link> <br />
                            <Link href="/">Privacy Policy</Link> <br />
                            <Link href="/">Terms & Conditions</Link>
                        </div>
                        <div>
                            <p>Extras</p>
                            <Link href="/">About Us</Link> <br />
                            <Link href="/">Information</Link> <br />
                            <Link href="/">Privacy Policy</Link> <br />
                            <Link href="/">Terms & Conditions</Link>
                        </div>
                        <div>
                            <p>My Account</p>
                            <Link href="/">About Us</Link> <br />
                            <Link href="/">Information</Link> <br />
                            <Link href="/">Privacy Policy</Link> <br />
                            <Link href="/">Terms & Conditions</Link>
                        </div>
                        <div>
                            <p>Useful Links</p>
                            <Link href="/">About Us</Link> <br />
                            <Link href="/">Information</Link> <br />
                            <Link href="/">Privacy Policy</Link> <br />
                            <Link href="/">Terms & Conditions</Link>
                        </div>
                        <div>
                            <p>Our Offers</p>
                            <Link href="/">About Us</Link> <br />
                            <Link href="/">Information</Link> <br />
                            <Link href="/">Privacy Policy</Link> <br />
                            <Link href="/">Terms & Conditions</Link>
                        </div>
                    </div>
                </div>
            </div>
        </TopFooterWrapper>
    )
}

export default TopFooter;
