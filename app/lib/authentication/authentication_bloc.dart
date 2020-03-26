import 'package:bloc/bloc.dart';
import 'package:eletec/repository/token.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/foundation.dart';

part 'authentication_event.dart';
part 'authentication_state.dart';

class AuthenticationBloc
    extends Bloc<AuthenticationEvent, AuthenticationState> {
  AuthenticationBloc();

  @override
  AuthenticationState get initialState => AuthenticationUninitialized();

  @override
  Stream<AuthenticationState> mapEventToState(
    AuthenticationEvent event,
  ) async* {
    if (event is AppStarted) {
      final String token = await TokenRepository().get();

      if (token != 'unknow') {
        yield AuthenticationAuthenticated();
      } else {
        yield AuthenticationUnauthenticated();
      }
    }

    if (event is LoggedIn) {
      yield AuthenticationLoading();
      await TokenRepository().set(event.token);
      yield AuthenticationAuthenticated();
    }

    if (event is LoggedOut) {
      yield AuthenticationLoading();
      await TokenRepository().clear();
      yield AuthenticationUnauthenticated();
    }
  }
}
