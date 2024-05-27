import { ReactNode, useEffect } from "react";
import { Navigate, useNavigate } from "react-router";
import { useAuth } from "src/utils/auth";

type Props = {
    children: ReactNode
}

export const AuthMiddleware = ({ children }: Props) => { 
    const navigate = useNavigate();
    const { isLogged } = useAuth();

    useEffect(() => {
        if (!isLogged) navigate('/signin')
    },[])

    // if (!isLogged) {
    //     return (
    //         <Navigate to='/signin' replace />
    //     )
    // }

    return (
        <>
            {children}
        </>
    );
}