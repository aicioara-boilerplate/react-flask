import * as template from 'actions/templateAction.jsx';

const initialState = {
    value: 0,
    dinosaurs: [],
};

export default (state=initialState, action) => {
    switch(action.type) {
    case template.CHANGE_VALUE: {
        return {
            ...state,
            value: action.payload,
        }
    }
    case template.LIST_DINOSAURS_SUCCESS: {
        return {
            ...state,
            dinosaurs: action.payload,
        }
    }
    default:
        return state;
    }
};
