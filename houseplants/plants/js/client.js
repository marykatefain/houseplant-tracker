import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { setContext } from 'apollo-link-context'
import { InMemoryCache } from 'apollo-cache-inmemory'
import cookie from 'cookie'

const httpLink = createHttpLink({
  uri: '/graphql'
})

const authLink = setContext(() => {
  return {
    headers: {
      'X-CSRFToken': cookie.parse(document.cookie).csrftoken
    }
  }
})

export default new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
})
