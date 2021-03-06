import { applyMiddleware, compose, createStore } from 'redux';
import { persistReducer, persistStore } from 'redux-persist';
import storage from 'redux-persist/es/storage';
import { routerMiddleware } from 'connected-react-router';
import { apiMiddleware } from 'redux-api-middleware';

import getRootReducer from 'reducers/reducers.jsx';

export default (history) => {
    const rootReducer = getRootReducer(history)

    const persistedReducer = persistReducer({
        key: 'polls',
        storage: storage,
        whitelist: [''], // Add name of reducers here
    }, rootReducer);

    const store = createStore(
        persistedReducer,
        {},
        compose(
            applyMiddleware(
                apiMiddleware,
                // routerMiddleware(history)
            ),
            window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
        )
    );

    const persistor = persistStore(store);

    return {store, persistor};
};