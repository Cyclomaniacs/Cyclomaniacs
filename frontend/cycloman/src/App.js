import logo from './logo.svg';
import './App.css';
import { Container } from 'semantic-ui-react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import 'semantic-ui-css/semantic.min.css';
import landing from './components/landing';
import results from './components/results';


function App() {
  return (
		<Router>
			<Container>
				<Route exact path="/" component={landing} />
				<Route path="/results" component={results} />
				{/* <Route exact path="/adminHome" component={adminHome} />
				<Route exact path="/orderSum" component={orderSum} />
				<Route exact path="/resetPW/*" component={resetPW} /> */}
			</Container>
		</Router>
  );
}

// export default App;
// import React from 'react';
// import { Container } from 'semantic-ui-react';
// import { BrowserRouter as Router, Route } from 'react-router-dom';
// import 'semantic-ui-css/semantic.min.css';
// import adminHome from './Pages/adminHome';
// import orderSum from './Pages/orderSum';
// import forgotPW from './Pages/forgotPW';
// import loginScreen from './Pages/loginScreen';
// import resetPW from './Pages/resetPW';

// function App() {
// 	return (

// 	);
// }

export default App;