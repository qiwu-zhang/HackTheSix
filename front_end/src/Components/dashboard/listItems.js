import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import PeopleIcon from '@material-ui/icons/People';
import BarChartIcon from '@material-ui/icons/BarChart';
import LayersIcon from '@material-ui/icons/Layers';
import AssignmentIcon from '@material-ui/icons/Assignment';
import { makeStyles } from '@material-ui/core/styles';
import {
  BrowserRouter as Router,
  Link,
  Switch,
  Route,
  useRouteMatch, useLocation,
} from "react-router-dom";

const useStyles = makeStyles({
  noUnderline: {
    textDecoration: "none"
  },
  listItem : {
    maxHeight: "45px", 
  }
});
const LinkNoUnderline = ({path}) => {
  const classes = useStyles();
  return(<Link className={classes.noUnderline} to={path}></Link>);
};

const MainListItems = ({pathName}) => {
  const location = useLocation();
  const classes = useStyles();
  let {path, url} = useRouteMatch();
  return (
  <React.Fragment>
    <ListItem className={classes.listItem}button>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <Link to={`/${pathName}`}><ListItemText primary="Dashboard"/></Link>
    </ListItem>
    <ListItem className={classes.listItem}button>
      <ListItemIcon>
        <ShoppingCartIcon />
      </ListItemIcon>
      <Link to={`/${pathName}/stocks`}><ListItemText primary="Stocks"/></Link>
    </ListItem>
    <ListItem className={classes.listItem}button>
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <Link to={`/${pathName}/transactions`}><ListItemText primary="Transactions"/></Link>
    </ListItem>
    <ListItem className={classes.listItem}button>
      <ListItemIcon>
        <BarChartIcon />
      </ListItemIcon>
      <Link to={`/${pathName}/reports`}><ListItemText primary="Reports"/></Link>
    </ListItem>
    <ListItem className={classes.listItem}button>
      <ListItemIcon>
        <LayersIcon />
      </ListItemIcon>
      <Link to={`/${pathName}/chatbot`}><ListItemText primary="Chatbot"/></Link>
    </ListItem>
  </React.Fragment>);
};

const secondaryListItems = (
  <div>
    <ListSubheader inset>Saved reports</ListSubheader>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Current month" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Last quarter" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Year-end sale" />
    </ListItem>
  </div>
);

export {
  MainListItems,
  secondaryListItems,
}