import React from 'react';

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <div>
                    App
                </div>
                <button className='btn btn-primary' onClick={() => this.props.listDinosaurs()}>List Dinosaurs</button>
                <pre>
                    {JSON.stringify(this.props.dinosaurs)}
                </pre>
            </div>
        )
    }

    componentDidMount() {

    }
}

App.defaultProps = {
    dinosaurs: [],
    listDinosaurs: () => {},
}

import {connect} from 'react-redux';
import {listDinosaurs} from 'actions/templateAction.jsx'

const mapStateToProps = state => ({
    dinosaurs: state.template.dinosaurs,
});

const mapDispatchToProps = dispatch => ({
    listDinosaurs: () => dispatch(listDinosaurs()),
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
