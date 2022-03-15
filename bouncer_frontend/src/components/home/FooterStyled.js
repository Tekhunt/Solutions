import styled from 'styled-components';

export const FooterWrapper = styled.section`
    .footer-bottom {
        max-width: 1200px;
        margin: 20px auto;
        padding: 0 2rem; 
    }
    .footer-bottom > div{
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }

    .footer-bottom div > div:last-child a{
        margin: 0 5px;
    }

`