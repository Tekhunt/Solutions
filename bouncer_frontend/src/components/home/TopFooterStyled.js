import styled from 'styled-components';

export const TopFooterWrapper = styled.section `
    margin-bottom: 20px;
    .container{
        max-width: 1200px;
        margin: 0px auto;
        padding: 0 2rem;  
    }

    .footer-top{
        padding: 30px 0;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-column-gap: 50px;
    }
    .footer-top div >p{
        margin: 30px 0 0 0;
    }
    .footer-top .fab{
        color:#33A0FF;
    }
    .footer-top .twitter-icon > .fab{
        color: rgb(29, 29, 167);
        padding-top: 10px;
        margin-left: 1.2rem;   
    }
    .footer-line{
        max-width: 100%;
        margin: 15px auto;
        background-color:grey;
        height: 2px;
    }
    .footer-link > div{
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        grid-column-gap: 50px;
    }
    .footer-link p {
        margin: 10px 0;
    }
    .footer-link a {
        text-decoration: none;
        color: rgb(193, 200, 206);
        font-size: 0.875rem;
    }
    .footer-link a:hover{
        color: black;
    }

    @media only screen and (max-width: 767px){
        .footer-top{
            padding: 30px 0;
            display: grid;
            grid-template-columns: 1fr;
            margin: 20px 0;
        }
        .footer-link > div{
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-column-gap: 50px;
        }
        .footer-top .footer-text{
            margin-top: 20px;
        }

        .footer-top div >p{
          margin: 10px 0 0 0;
        }
    }
    
`