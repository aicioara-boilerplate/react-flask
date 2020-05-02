import { RSAA } from 'redux-api-middleware';

export const CHANGE_VALUE = '@@template/CHANGE_VALUE';

export const LIST_DINOSAURS_REQUEST = '@@api/LIST_DINOSAURS_REQUEST';
export const LIST_DINOSAURS_SUCCESS = '@@api/LIST_DINOSAURS_SUCCESS';
export const LIST_DINOSAURS_FAILURE = '@@api/LIST_DINOSAURS_FAILURE';


export const changeValue = () => ({
    type: CHANGE_VALUE,
    payload: 1,
});


export const listDinosaurs = () => ({
    [RSAA]: {
        endpoint: '/api/dinosaurs/',
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        types: [ LIST_DINOSAURS_REQUEST, LIST_DINOSAURS_SUCCESS, LIST_DINOSAURS_FAILURE ],
    }
});
