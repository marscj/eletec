import 'dart:async';
import 'package:bloc/bloc.dart';
import 'package:eletec/repository/token.dart';

import 'store.dart';

class StoreBloc extends Bloc<AuthenticationEvent, AuthenticationState> {
  StoreBloc();

  @override
  AuthenticationState get initialState => AuthenticationUninitialized();

  @override
  Stream<AuthenticationState> mapEventToState(
    AuthenticationEvent event,
  ) async* {
    if (event is AppStarted) {
      final String token = await TokenRepository().getToken();

      if (token != 'unknow') {
        yield AuthenticationAuthenticated();
      } else {
        yield AuthenticationUnauthenticated();
      }
    }

    if (event is LoggedIn) {
      yield AuthenticationLoading();
      await TokenRepository().setToken(event.token);
      yield AuthenticationAuthenticated();
    }

    if (event is LoggedOut) {
      yield AuthenticationLoading();
      await TokenRepository().clearToken();
      yield AuthenticationUnauthenticated();
    }
  }
}
