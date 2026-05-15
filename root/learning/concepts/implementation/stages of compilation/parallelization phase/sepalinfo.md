The fourth step of compilation is automatic parallelization.

After the automatic borrow-checker has labelled every read and write, the next phase is to string all of this information together.

A directed acyclic graph (DAG) is created, stringing together each item that was labeled by the borrow checker.
// A DAG is created by line number. This is extremely difficult to explain. Please explain this in a way that's simple. It's really easy to show visually, but English aint it.
// Also explain why a non-dag is literally impossible under this model. It's difficult to explain.

When you write Trillia, you may not even be aware that everything is parallelized.
The syntax is very clean and minimal, and there's basically nothing that would indicate parallelism unless you know what to look for.
The result of a parallelized implementation of Trillia is always the same as a non-parallelized implementation.

During this phase of compilation, each line of code is reordered to be more easily read in parallel by interpreters.



