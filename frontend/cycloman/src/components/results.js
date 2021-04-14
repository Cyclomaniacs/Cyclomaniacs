import React from 'react';
import { useState } from 'react';
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import {
	Grid,
	Header,
	Form,
	Segment,
	Button,
} from 'semantic-ui-react';

// function Results( {query}) {
    
//     return(
//         <div>
//         <h1>Please help me Im stuck in a washing machine</h1>
//         <h2>{query}</h2>
//         </div>
//     );
// }

class Results extends React.Component {
    constructor(props) {
        super(props);
    
    }


    
    render() {
        console.log(this.props.location.state)
        return (
            <div>
                <h1> This is a test</h1>
                <h2>You Searched For : {this.props.location.state}</h2>
            </div>
        )
    }
}

//you spelt default wrong lmao. I'm going to get taco bell brb
export default Results;