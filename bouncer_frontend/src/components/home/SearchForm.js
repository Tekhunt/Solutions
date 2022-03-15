import React from 'react'
import { FormWrapper } from './SearchFormStyled';

function SearchForm() {
    return (
        <FormWrapper>
            <div className="input-product">
                <input type="text" placeholder="Search query..." />
                <input type="submit" value="Search" />
            </div>
        </FormWrapper>
    )
}

export default SearchForm;