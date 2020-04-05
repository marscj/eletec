part of 'loading_bloc.dart';

class LoadingState extends Equatable {
  final bool loading ;

  @override
  List<Object> get props => [loading];

  LoadingState({
    this.loading
  });

  factory LoadingState.initial() => LoadingState(loading: false);

  factory LoadingState.showDialog() => LoadingState(loading: true);

  factory LoadingState.dismissDialog() => LoadingState(loading: false);
}
