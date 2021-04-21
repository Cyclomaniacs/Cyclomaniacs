import React from 'react';
import {
	Grid,
	Header,
  Image
} from 'semantic-ui-react';
import AustinImage from './SullivanPicture.jpg';
import XavierImage from './XavierPicture.jpg';
import NicholasImage from './NicholasPicture.jpg';
import NorlandImage from './NorlandImage.jpg';
import ColinImage from './ColinPicture.JPG';

function aboutUs() {

    const style = {
		h1: {
			marginBottom: '2em', marginTop: '-100px',
		},
		Button: {
			marginBottom: '1em',
		},
	};

    return (
        <div>
    
    <div style={{height: 70}}></div>
    
    <Grid columns='five' divided>

    <Grid.Row>
      <Grid.Column verticalAlign = "bottom">
        <Image src= {AustinImage} />
      </Grid.Column>
      <Grid.Column verticalAlign = "bottom">
        <Image src={NorlandImage} />
      </Grid.Column>
      <Grid.Column verticalAlign = "bottom">
        <Image src={NicholasImage} />
      </Grid.Column>
      <Grid.Column verticalAlign = "bottom">
        <Image src={XavierImage} />
      </Grid.Column>
      <Grid.Column verticalAlign = "bottom">
        <Image src={ColinImage} />
      </Grid.Column>
    </Grid.Row>

    <Grid.Row>
      <Grid.Column>

        <Header> Austin Sullivan </Header>
        <p>
        Austin Sullivan is on his last year studying Computer Science at the University of Florida. Upon graduation, Mr. Sullivan will be commissioning 
        into the United States Marine Corps as a 2nd Lieutenant and is slated to become a Naval Aviator within the next few years. Further down his career, 
        he plans on attending Test Pilot School in the hopes of one day being selected for the Astronaut Program. He has had numerous experiences working 
        with C++ and Java with his undergraduate classes at the University of Florida and plans to use them as his Marine Corps career progresses.
        </p>
      </Grid.Column>
      <Grid.Column>
        <Header> Norland Batista </Header>
        <p>
         Norland Batista is graduating from the University of Florida with a Bachelor’s in Computer Science with a 3.5 GPA. 
         Currently he has no set-in-stone destinations for work which is why his next steps are to seek his very first full-time employment
         opportunity after graduation and work as a software engineer. Other personal interests include guitar, drawing, soccer, and 
         going on adventures with friends.
        </p>
      </Grid.Column>
      <Grid.Column>
        <Header> Nicholas Miller </Header> 
        <p>
        A 5th Year computer science major at the University of Florida. Nicholas has had internships at People 2.0, Oak Ridge National Laboratories, 
        and L3Harris where he is scheduled to work after graduation, where he will be a part of the three year IT Leadership Program. Nicholas loves history, 
        philosophy, and creative pursuits.
        </p>
      </Grid.Column>
      <Grid.Column>
        <Header> Xavier Adams-Stewart </Header>
        <p>        
        Xavier Adams-Stewart was born in Rockledge, Florida on April 7, 1999. 
        He completed his high school education at Niceville Senior High School in Niceville, Florida. 
        At the time of creating this website, he was completing his bachelor’s degree in Computer Science at the University of Florida in Gainesville, Florida.
        Xavier has an interest in software engineering and cybersecurity, and is working to complete a multitude of CompTIA certification exams. 
        He is competent in Java, C++, and C, as well as technical presentations. 
        He enjoys playing video games, listening to music, playing instruments, and listening to podcasts. 
        </p>
      </Grid.Column>
      <Grid.Column>
        <Header> Colin Adams </Header>
        <p>
        Colin Adams is completing his degree in Computer Science from the University of Florida. 
        Colin is a passionate individual that loves to tackle new technologies and interesting problems. 
        Last summer, Colin spent his time freelancing data science on Upwork while living nomadically. 
        He plans on gaining employment in Denver, Colorado doing software engineering. He is proficient in Python, 
        C++, JavaScript, and Java. Colin enjoys hiking, cycling, climbing, and touring when he is not tackling problems 
        at the computer. He hopes to live remotely in the mountains while also working for a cause that is meaningful and impactful.
        </p>
      </Grid.Column>
    </Grid.Row>
  </Grid>
        </div>
    );
}


export default aboutUs;