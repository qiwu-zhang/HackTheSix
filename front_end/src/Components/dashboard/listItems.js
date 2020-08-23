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
  useHistory
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
  const history = useHistory();
  const classes = useStyles();
  let {path, url} = useRouteMatch();
  return (
  <React.Fragment>
    <ListItem className={classes.listItem} onClick={() => history.push(`/${pathName}`)}onCLickbutton>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard"/>
    </ListItem>
    <ListItem className={classes.listItem} onClick={() => history.push(`/${pathName}/stocks`)}button>
      <ListItemIcon>
        <ShoppingCartIcon />
      </ListItemIcon>
      <ListItemText primary="Stocks"/>
    </ListItem>
    <ListItem className={classes.listItem} onClick={() => history.push(`/${pathName}/transactions`)}button>
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="Transactions"/>
    </ListItem>
    <ListItem className={classes.listItem}  onClick={() => history.push(`/${pathName}/reports`)} button>
      <ListItemIcon>
        <BarChartIcon />
      </ListItemIcon>
      <ListItemText primary="Reports"/>
    </ListItem>
    <ListItem className={classes.listItem} onClick={() => history.push(`/${pathName}/chatbot`)}button>
      <ListItemIcon>
        <LayersIcon />
      </ListItemIcon>
      <ListItemText primary="Chatbot"/>
    </ListItem>
    <ListItem className={classes.listItem} onClick={() => history.push(`/${pathName}/savingsplans`)}button>
      <ListItemIcon>
        <LayersIcon />
      </ListItemIcon>
      <ListItemText primary="Savings Plans"/>
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