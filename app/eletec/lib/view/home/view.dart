import 'package:eletec/authentication/authentication_bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../view.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) =>
      BlocListener<AuthenticationBloc, AuthenticationState>(
          listener: (context, state) {},
          child: BlocBuilder<AuthenticationBloc, AuthenticationState>(
            builder: (context, state) {
              // if (state is AuthenticationAuthenticated) {
              //   return Container(
              //     child: Text('home'),
              //   );
              // }
              // if (state is AuthenticationUnauthenticated) {
              //   return LoginPage();
              // }
              // return Container(
              //   child: Text('data'),
              // );
              return LoginPage();
            },
          ));
}
