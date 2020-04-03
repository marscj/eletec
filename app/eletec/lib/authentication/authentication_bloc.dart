import 'package:bloc/bloc.dart';
import 'package:eletec/rest/client.dart';
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
      final String token = await CacheService.instance.getToken();

      if (token != 'unknow') {
        yield AuthenticationAuthenticated();
      } else {
        yield AuthenticationUnauthenticated();
      }
    }

    if (event is LoggedIn) {
      await CacheService.instance.setToken(event.token);
      yield AuthenticationAuthenticated();
    }

    if (event is LoggedOut) {
      await CacheService.instance.clearToken();
      yield AuthenticationUnauthenticated();
    }
  }
}
