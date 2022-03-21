

export default function Layout(props: any){
    return (
        <>
            <div>
                <main>
                    {props.children}
                </main>
            </div>
        </>
    )
}