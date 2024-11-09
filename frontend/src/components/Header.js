import React, {Component} from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import AutoStoriesIcon from '@mui/icons-material/AutoStories';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import {Badge, IconButton} from "@mui/material";
import PropTypes from "prop-types";


export default class Header extends Component {

    static propTypes = {
        onActionDo: PropTypes.func.isRequired,
        cartSize: PropTypes.number.isRequired,
    };

    render() {
        return <header>
            <AppBar position="static">
                <Toolbar>
                    <AutoStoriesIcon sx={{mr: 2}}/>
                    <Typography variant="h6" color="inherit" sx={{ flexGrow: 1 }}>
                        Fiuba Editorial
                    </Typography>
                    <IconButton
                        size="large"
                        aria-label="account of current user"
                        aria-controls="menu-appbar"
                        aria-haspopup="true"
                        color="inherit"
                        onClick={() => this.props.onActionDo()}
                    >
                        <Badge badgeContent={this.props.cartSize} color="secondary">
                            <ShoppingCartIcon/>
                        </Badge>
                    </IconButton>
                </Toolbar>
            </AppBar>
        </header>
    }
}