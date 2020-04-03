import 'package:eletec/view/app/app.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../view.dart';

class HomeHookPage extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) => BlocListener<AppBloc, AppState>(
    listener: (context, state) {},
    child: BlocBuilder<AppBloc, AppState>(
      builder: (context, state) {
        if (state.signedIn) {
          return HomePage();
        } else {
          return LoginPage();
        }
      },
    )
  );
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
    body: Center(
      child: RaisedButton(
        child: Text('LogOUT'),
        onPressed: () => BlocProvider.of<AppBloc>(context).add(SignedOut()),
      ),
    ),
  );
}