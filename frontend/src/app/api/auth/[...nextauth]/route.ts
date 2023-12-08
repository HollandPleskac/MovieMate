import NextAuth from "next-auth/next";
import GithubProvider from "next-auth/providers/github";

const handler = NextAuth({
    providers: [
        GithubProvider({
            clientId: process.env.GITHUB_ID ?? "",
            clientSecret: process.env.GITHUB_SECRET ?? ""
        })
    ],
    callbacks: {
        async session({ session, token, user }) {
            console.log("LOG SESSION",session)
            console.log(session.user?.name, session.user?.email)
            // add user to db
            try {
                const response = await fetch('http://127.0.0.1:8000/create-user', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({ email: session.user?.email })
                });
                const data = await response.json();
                console.log("Success:",data);
              } catch (error) {
                console.error('Error creating user:', error);
              }
            return session
        },
      }
})

export {handler as GET, handler as POST}