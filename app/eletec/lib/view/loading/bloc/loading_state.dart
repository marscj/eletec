part of 'loading_bloc.dart';

class LoadingState extends Equatable {
  final bool loading ;

  @override
  List<Object> get props => [];

  LoadingState({
    this.loading
  });

  factory LoadingState.initial() => LoadingState(loading: false);
}
