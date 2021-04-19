import React from 'react';
import { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { useHistory } from 'react-router-dom';
import results from './results'
import '../App.css';


import {
	Grid,
	Header,
	Form,
	Segment,
	Button,
} from 'semantic-ui-react';


class Landing extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            query: ""
        };
    }
        
        // const [query, setQuery] = useState();
        // const history = useHistory()
    
    search = (evt) => {
        console.log("The button was clicked");
        if (this.state.query) // if the user has actually typed something
        {
            console.log('It worked')
            console.log(this.state.query)
        }
        else
        {
            console.log('Please input something')
        }
        
        this.props.history.push({pathname: '/results', state: this.state.query})
        


        //stuff
    };

    readInput = (evt) => {
        // console.log(evt);
        this.setState({query : evt.target.value });
        console.log(this.state.query);

    };



    render () {

        // const bodystyle = {
        //     color: "yellow"
        // }
        return(
        <div>
              <title>Cyclomaniacs</title>

            <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet"></link>
            <link href="css/scrolling-nav.css" rel="stylesheet"></link>
            
            <body id="page-top">

                <div class="container text-center">

                    <div id="login">

                    <img src="logo4.PNG" class="m-0 text-center" alt="Cyclomaniacs Logo" width="615" height="249"></img>
                    <Form size = "large">
                        <Segment stacked>
                            <Form.Input
                            placeholder="Search Query"
                            onChange={this.readInput.bind(this)}
                            />
                        </Segment>
                    </Form>
                    {/* <form action="javascript:void(0);" method="get">
                        
                        <input type="text" placeholder="Search for bike products here and we will find the lowest prices..." name="search" size="50">
                        </input> */}
                        {/* <button class="test1 center">Search</button> */}
                        <Button
                        color = "blue"
                        onClick = {this.search}>
                            Search
                            </Button>
                            <Button
                            color = 'grey'
                            size = 'medium'
                            href ="/aboutUs"
                            >
                                About Us
                            </Button>
                            

                    {/* </form> */}


                    </div>

                </div>
                <script src="vendor/jquery/jquery.min.js"></script>
                <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

                <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

                <script src="js/scrolling-nav.js"></script>
                </body>
        
        </div>
        ) 
    };
}


export default Landing;