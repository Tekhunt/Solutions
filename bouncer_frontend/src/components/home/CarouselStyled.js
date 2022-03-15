import styled from 'styled-components';


export const SliderWrapper = styled.section`
    img {
        object-fit: contain;
        width: 100%;
    }
    .container-hero{
        transform: translateY(-50px);
        max-width: 1200px;
        margin: 0px auto;
    }
    .hero-category {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr; 
    }

    @media only screen and (max-width: 767px){
        .container-hero{
            
            padding: 0 2rem; 
        }
        
    }

`