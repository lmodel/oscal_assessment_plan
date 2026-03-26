package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A human-oriented, globally unique identifier for a system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemId  {

  private String id;
  private String identifier-type;

}