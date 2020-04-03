part of 'app_bloc.dart';

abstract class AppEvent extends Equatable {
  const AppEvent();
}

class AppInitial extends AppEvent {

  @override
  List<Object> get props => [];
}

class LocaleUpdate extends AppEvent {
  final String languageCode;

  LocaleUpdate(this.languageCode);

  @override
  List<Object> get props => [languageCode];
}

class SignedIn extends AppEvent {
  final String token;

  SignedIn(this.token);

  @override
  List<Object> get props => [token];

}

class SignedOut extends AppEvent {
  @override
  List<Object> get props => [];
}