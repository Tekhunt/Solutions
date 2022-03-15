import React from 'react'
import { Link } from 'react-router-dom';
import { FooterWrapper } from './FooterStyled';

function Footer() {
    return (
        <FooterWrapper>
            <div className="footer-bottom">
                <div>
                    <div>
                        <p>
                            © 2018 Ecommerce theme by www.bisenbaev.com
                        </p>
                    </div>
                    <div>
                        <Link href="/"> 
                             <img src="img/Western-union.4fe21200.svg" alt="Western-union pic" />
                        </Link>
                        <Link href="/">
                            <img src="img/mastercard.f8415f65.svg" alt="mastercard pic" />
                        </Link>
                        <Link href="/">
                             <img src="img/Paypal.50d087dc.svg" alt="aypal pic" />
                         </Link>
                        <Link href="/">
                            <img src="img/visas.63f8784c.svg" alt="visas pic" />
                        </Link>
                    </div>
                </div>
            </div>
        </FooterWrapper>
    )
};

export default Footer;
