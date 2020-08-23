/* Our Components */
import { DashInfo } from "./DashInfo";
import React, {useState, useEffect} from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import Button from "@material-ui/core/Button"
import ButtonGroup from "@material-ui/core/ButtonGroup"
import Box from '@material-ui/core/Box';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import {Link as ALink} from '@material-ui/core/';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import NotificationsIcon from '@material-ui/icons/Notifications';
import { MainListItems, secondaryListItems } from './listItems'
import {BrowserRouter as Router, Link, Switch, useRouteMatch, useLocation, Route} from "react-router-dom";
import KeyboardArrowDownIcon from '@material-ui/icons/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';

// import Chart from "./Chart";
import Transactions from "./Transactions";

const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    width: '100vw',
    paddingLeft: 0,
    paddingRight: 0,
    overflowX: "hidden",
  },

  centerFlex : {
    justifyContent: "center",
  },

  toolbar: {
    paddingRight: 24, // keep right padding when drawer closed
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: "100vw",
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: 36,
  },
  menuButtonHidden: {
    display: 'none',
  },
  title: {
    flexGrow: 1, // Space assigned to a child in a flexBox. Ex. 2 would take up more space than 1
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: theme.spacing(7),
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9),
    },
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',

  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
  loginButton : {
    fontWeight: 700
  },

  fixedFContainer : {
    bottom: "0px",
    visibility: "visible"
  },

  noFContainer : {
    bottom: "-40px",
    visibility: "hidden"
  },

  footerContainer : {
    background: theme.palette.primary.dark,
    opacity: 0.7,
    width: "100vw",
    height: "40px",
    position: "fixed",
    transition: "position 1s ease-out"
  },

  footer : {
    color: "white",
    position: "fixed",
    bottom: "10px",
    left : `calc(48%)`,
  },

  smallPaper : {
    width: "35px",
    height: "35px",
  },

  smallPaperBottom : {
    bottom: "0px",
  },

  bigPaperBottom: {
    bottom: "40px"
  },

  stickyPaper: {
    position: "fixed",
    right: "0px",
  }, stickyPaperHover:{
    boxShadow: "0px 0px 1px inset",
    transition: "boxShadow 2s",
  }
  
}));

function Copyright() {
  const [visibility, setVisibility] = useState(true);
  const [hoverSticky, setHoverSticky] = useState(false);

  const classes = useStyles();  
  return (
    <React.Fragment>
    <Paper className={clsx(classes.smallPaper, classes.stickyPaper, hoverSticky && classes.stickyPaperHover, !visibility && classes.smallPaperBottom || classes.bigPaperBottom)} 
      onMouseEnter={() => setHoverSticky(true)}
      onMouseOut={() => setHoverSticky(false)}
      onClick={() => setVisibility(!visibility)} >

      {visibility && <KeyboardArrowDownIcon fontSize="large"/> || <KeyboardArrowUpIcon fontSize="large"/>}
    </Paper>
    <Container className={clsx(visibility ? classes.fixedFContainer : classes.noFContainer, classes.footerContainer)}>
    <div className={classes.footer}>
    <Typography variant="body2" align="center">
      {'Copyright © '}
      <ALink style={{color: "white"}}href="https://material-ui.com/">
        Your Dashboard
      </ALink>
      {" "}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
    
    </div>
    </Container>
    </React.Fragment>
  );
}

export default function Dashboard() {
  const location = useLocation();
  let [pathName, setPathName] = useState(location.pathname.split("/").slice(-1)[0]);
  const classes = useStyles();
  const [open, setOpen] = React.useState(true);

  useEffect(() => {
    async function load(){
      await setPathName(location.pathname.split("/").slice(-1)[0]);
      console.log(pathName);
    }
    load()
  }, []);

  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  if (pathName.toLowerCase() !== "dashboard"){
    return (
      <Router>
      <div className={classes.root}>
      <CssBaseline />
      <AppBar position="absolute" className={clsx(classes.appBar, open && classes.appBarShift)}>
        <Toolbar className={classes.toolbar}>
          <IconButton
            edge="end"
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
          >
            <MenuIcon />
          </IconButton>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
            Dashboard
          </Typography>
          <IconButton color="inherit">
            <Badge badgeContent={5} color="secondary">
              <NotificationsIcon />
            </Badge>
          </IconButton>
        </Toolbar>
      </AppBar>
     
          <Drawer
            variant="permanent"
            classes={{
              // clsx seems to combine a bunch of styles together 
              paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
            }}
            open={open}
          >
          
          <div className={classes.toolbarIcon}>
            <IconButton onClick={handleDrawerClose}>
              <ChevronLeftIcon />
            </IconButton>
          </div>
          <Divider />
          <List><MainListItems pathName={pathName}/></List>
          <Divider />
          <List>{secondaryListItems}</List>
        </Drawer>
        <main className={classes.content}>
          <div className={classes.appBarSpacer} />
          <Container maxWidth="lg" className={classes.container}>
            <Route exact path={`/${pathName}`}><DashInfo/></Route>
            <Route exact path={`/${pathName}/stocks`}>Stocks</Route>
            <Route exact path={`/${pathName}/transactions`}><Transactions/></Route>
            <Route exact path={`/${pathName}/reports`}>Reports</Route>
            <Route exact path={`/${pathName}/chatbot`}>Chatbot</Route>
            <Box pt={4}>
            </Box>
          </Container>
          <Copyright />
            
        </main>
      
    </div>
    </Router>
    );
  }

  return (<h1>ERROR, YOU MUST LOGIN BEFORE YOU ACCESS THE DASHBOARD</h1>)
}
