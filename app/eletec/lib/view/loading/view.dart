
import 'package:eletec/view/loading/bloc/loading_bloc.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class LoadingWidget extends StatelessWidget {
  final Widget child;

  const LoadingWidget({Key key, this.child}) : super(key: key);
  
  @override
  Widget build(BuildContext context) => BlocProvider<LoadingBloc>(
   create: (state) => LoadingBloc(),
   child: BlocBuilder<LoadingBloc, LoadingState> (
    builder: (context, state) {
        return Directionality(
        textDirection: TextDirection.ltr,
        child: Overlay(
          key: BlocProvider.of<LoadingBloc>(context).overlayKey,
          initialEntries: [
            OverlayEntry(
              builder: (context) => child
            )
          ],
        ));
      }
    )
  );
  
}